# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 437
- HTTP: 103 alive / 85 gold
- HTTPS: 50 alive / 30 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49443
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
