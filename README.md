# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 439
- HTTP: 112 alive / 86 gold
- HTTPS: 53 alive / 32 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49442
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
