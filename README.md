# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 421
- HTTP: 101 alive / 67 gold
- HTTPS: 48 alive / 20 gold
- SOCKS4: 192 alive / 163 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48918
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
