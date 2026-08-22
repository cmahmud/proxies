# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 424
- HTTP: 340 alive / 88 gold
- HTTPS: 212 alive / 24 gold
- SOCKS4: 240 alive / 141 gold
- SOCKS5: 307 alive / 171 gold

## Historical pool

- Discovered: 164947
- Ever alive: 32217
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
