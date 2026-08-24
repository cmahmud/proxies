# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 387
- HTTP: 125 alive / 49 gold
- HTTPS: 53 alive / 13 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33583
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
