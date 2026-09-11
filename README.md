# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 428
- HTTP: 104 alive / 72 gold
- HTTPS: 36 alive / 20 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48929
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
