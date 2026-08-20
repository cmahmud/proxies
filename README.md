# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 354
- HTTP: 220 alive / 71 gold
- HTTPS: 117 alive / 17 gold
- SOCKS4: 192 alive / 131 gold
- SOCKS5: 182 alive / 135 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25777
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
