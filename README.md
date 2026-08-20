# SyndProxy private pool

## Current pool

- Alive now: 715
- Gold now: 350
- HTTP: 224 alive / 67 gold
- HTTPS: 118 alive / 16 gold
- SOCKS4: 192 alive / 131 gold
- SOCKS5: 181 alive / 136 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25776
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
