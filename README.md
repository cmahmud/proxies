# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 210
- HTTP: 136 alive / 34 gold
- HTTPS: 104 alive / 7 gold
- SOCKS4: 181 alive / 78 gold
- SOCKS5: 200 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32783
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
