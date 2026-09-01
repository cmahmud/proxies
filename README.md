# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 478
- HTTP: 150 alive / 97 gold
- HTTPS: 120 alive / 42 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46954
- Ever gold: 1460

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
