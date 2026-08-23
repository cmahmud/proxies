# SyndProxy validated proxy pool

## Current pool

- Alive now: 686
- Gold now: 198
- HTTP: 138 alive / 33 gold
- HTTPS: 128 alive / 6 gold
- SOCKS4: 205 alive / 68 gold
- SOCKS5: 215 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32782
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
