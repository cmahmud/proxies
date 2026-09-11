# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 373
- HTTP: 89 alive / 68 gold
- HTTPS: 48 alive / 23 gold
- SOCKS4: 144 alive / 112 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48726
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
