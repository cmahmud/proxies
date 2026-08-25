# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 417
- HTTP: 91 alive / 65 gold
- HTTPS: 50 alive / 19 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36741
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
