# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 429
- HTTP: 93 alive / 72 gold
- HTTPS: 42 alive / 20 gold
- SOCKS4: 192 alive / 163 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48922
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
