# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 461
- HTTP: 129 alive / 95 gold
- HTTPS: 64 alive / 32 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49342
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
