# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 462
- HTTP: 118 alive / 92 gold
- HTTPS: 51 alive / 32 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49427
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
