# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 376
- HTTP: 83 alive / 49 gold
- HTTPS: 38 alive / 12 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 198 alive / 161 gold

## Historical pool

- Discovered: 172309
- Ever alive: 32967
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
