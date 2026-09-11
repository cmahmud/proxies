# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 422
- HTTP: 98 alive / 71 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48949
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
