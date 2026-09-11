# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 425
- HTTP: 94 alive / 65 gold
- HTTPS: 52 alive / 22 gold
- SOCKS4: 197 alive / 166 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48909
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
