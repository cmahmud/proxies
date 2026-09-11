# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 420
- HTTP: 92 alive / 67 gold
- HTTPS: 41 alive / 21 gold
- SOCKS4: 187 alive / 161 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48876
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
