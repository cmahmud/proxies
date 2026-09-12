# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 462
- HTTP: 120 alive / 92 gold
- HTTPS: 51 alive / 30 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49427
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
