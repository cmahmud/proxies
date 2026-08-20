# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 350
- HTTP: 232 alive / 65 gold
- HTTPS: 119 alive / 15 gold
- SOCKS4: 194 alive / 133 gold
- SOCKS5: 179 alive / 137 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25775
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
