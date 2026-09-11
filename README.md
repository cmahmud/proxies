# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 422
- HTTP: 98 alive / 68 gold
- HTTPS: 36 alive / 18 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48961
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
