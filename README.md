# SyndProxy private pool

## Current pool

- Alive now: 757
- Gold now: 392
- HTTP: 178 alive / 78 gold
- HTTPS: 152 alive / 17 gold
- SOCKS4: 208 alive / 147 gold
- SOCKS5: 219 alive / 150 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26442
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
