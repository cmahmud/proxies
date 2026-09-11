# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 355
- HTTP: 106 alive / 72 gold
- HTTPS: 50 alive / 20 gold
- SOCKS4: 97 alive / 92 gold
- SOCKS5: 176 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48695
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
