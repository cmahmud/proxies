# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 414
- HTTP: 94 alive / 65 gold
- HTTPS: 50 alive / 17 gold
- SOCKS4: 192 alive / 161 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48882
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
