# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 376
- HTTP: 82 alive / 48 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 198 alive / 161 gold

## Historical pool

- Discovered: 172309
- Ever alive: 32967
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
