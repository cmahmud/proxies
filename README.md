# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 372
- HTTP: 82 alive / 45 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 172315
- Ever alive: 32973
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
