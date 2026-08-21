# SyndProxy private pool

## Current pool

- Alive now: 819
- Gold now: 412
- HTTP: 258 alive / 92 gold
- HTTPS: 138 alive / 22 gold
- SOCKS4: 207 alive / 147 gold
- SOCKS5: 216 alive / 151 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27823
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
