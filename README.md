# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 384
- HTTP: 96 alive / 67 gold
- HTTPS: 45 alive / 18 gold
- SOCKS4: 165 alive / 126 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48747
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
