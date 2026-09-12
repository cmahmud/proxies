# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 463
- HTTP: 123 alive / 90 gold
- HTTPS: 63 alive / 35 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49388
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
