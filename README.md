# SyndProxy private pool

## Current pool

- Alive now: 669
- Gold now: 387
- HTTP: 157 alive / 68 gold
- HTTPS: 92 alive / 16 gold
- SOCKS4: 197 alive / 143 gold
- SOCKS5: 223 alive / 160 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25791
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
