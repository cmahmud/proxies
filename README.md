# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 385
- HTTP: 321 alive / 79 gold
- HTTPS: 246 alive / 25 gold
- SOCKS4: 211 alive / 144 gold
- SOCKS5: 236 alive / 137 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32522
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
