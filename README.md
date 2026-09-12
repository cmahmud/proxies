# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 462
- HTTP: 123 alive / 92 gold
- HTTPS: 61 alive / 32 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49384
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
