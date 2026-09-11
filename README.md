# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 423
- HTTP: 95 alive / 65 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 194 alive / 166 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48911
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
