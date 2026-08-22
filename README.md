# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 445
- HTTP: 262 alive / 100 gold
- HTTPS: 163 alive / 25 gold
- SOCKS4: 217 alive / 157 gold
- SOCKS5: 237 alive / 163 gold

## Historical pool

- Discovered: 167121
- Ever alive: 32538
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
