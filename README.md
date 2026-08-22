# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 424
- HTTP: 260 alive / 86 gold
- HTTPS: 217 alive / 26 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 287 alive / 169 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32208
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
