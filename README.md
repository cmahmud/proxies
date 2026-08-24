# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 386
- HTTP: 98 alive / 57 gold
- HTTPS: 38 alive / 10 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33464
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
