# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 474
- HTTP: 172 alive / 102 gold
- HTTPS: 116 alive / 39 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 197 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45209
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
