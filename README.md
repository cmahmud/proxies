# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 460
- HTTP: 122 alive / 91 gold
- HTTPS: 60 alive / 31 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49384
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
