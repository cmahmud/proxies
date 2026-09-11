# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 402
- HTTP: 95 alive / 64 gold
- HTTPS: 35 alive / 20 gold
- SOCKS4: 163 alive / 144 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48784
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
