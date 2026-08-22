# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 387
- HTTP: 255 alive / 90 gold
- HTTPS: 251 alive / 26 gold
- SOCKS4: 187 alive / 128 gold
- SOCKS5: 206 alive / 143 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31360
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
