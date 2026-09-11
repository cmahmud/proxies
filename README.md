# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 425
- HTTP: 100 alive / 69 gold
- HTTPS: 35 alive / 20 gold
- SOCKS4: 187 alive / 164 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48927
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
