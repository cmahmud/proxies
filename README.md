# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 215
- HTTP: 148 alive / 33 gold
- HTTPS: 104 alive / 7 gold
- SOCKS4: 178 alive / 84 gold
- SOCKS5: 195 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32783
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
