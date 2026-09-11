# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 427
- HTTP: 103 alive / 74 gold
- HTTPS: 32 alive / 16 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48930
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
