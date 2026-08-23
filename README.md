# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 212
- HTTP: 151 alive / 33 gold
- HTTPS: 100 alive / 7 gold
- SOCKS4: 175 alive / 83 gold
- SOCKS5: 196 alive / 89 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32783
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
