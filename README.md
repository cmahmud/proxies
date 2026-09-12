# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 438
- HTTP: 109 alive / 86 gold
- HTTPS: 49 alive / 31 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49434
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
