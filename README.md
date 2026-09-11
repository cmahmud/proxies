# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 424
- HTTP: 87 alive / 67 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 189 alive / 166 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48894
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
