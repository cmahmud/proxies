# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 429
- HTTP: 88 alive / 69 gold
- HTTPS: 112 alive / 32 gold
- SOCKS4: 182 alive / 158 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47312
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
