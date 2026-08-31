# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 443
- HTTP: 116 alive / 77 gold
- HTTPS: 70 alive / 32 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45558
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
