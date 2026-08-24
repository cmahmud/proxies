# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 387
- HTTP: 127 alive / 50 gold
- HTTPS: 55 alive / 12 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33583
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
