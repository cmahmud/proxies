# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 417
- HTTP: 158 alive / 71 gold
- HTTPS: 87 alive / 18 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33840
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
