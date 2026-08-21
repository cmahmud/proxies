# SyndProxy private pool

## Current pool

- Alive now: 1117
- Gold now: 442
- HTTP: 402 alive / 112 gold
- HTTPS: 264 alive / 33 gold
- SOCKS4: 199 alive / 155 gold
- SOCKS5: 252 alive / 142 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28636
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
