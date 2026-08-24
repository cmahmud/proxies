# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 387
- HTTP: 120 alive / 59 gold
- HTTPS: 32 alive / 8 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 197 alive / 164 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33435
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
