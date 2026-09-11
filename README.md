# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 414
- HTTP: 87 alive / 64 gold
- HTTPS: 36 alive / 20 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 178 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48859
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
